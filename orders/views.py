from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Order, Cancellation
from .serializers import OrderSerializer, CancellationSerializer
from projects.models import Project


class OrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class OrderCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        project_id = request.data.get('project')
        area = request.data.get('area')

        try:
            project = Project.objects.get(id=project_id, is_active=True)
        except Project.DoesNotExist:
            return Response({'error': 'پروژه یافت نشد'}, status=status.HTTP_404_NOT_FOUND)

        price_per_meter = project.price_per_meter
        total_price = float(area) * float(price_per_meter)

        # بررسی اعتبار کاربر
        user = request.user
        if user.credit >= total_price:
            user.credit -= total_price
            user.save()
        else:
            return Response({'error': 'اعتبار کافی نیست'}, status=status.HTTP_400_BAD_REQUEST)

        order = Order.objects.create(
            user=user,
            project=project,
            area=area,
            price_per_meter=price_per_meter,
            total_price=total_price,
        )

        return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)


class OrderDetailView(generics.RetrieveAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class CancelOrderView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        try:
            order = Order.objects.get(id=pk, user=request.user, status='active')
        except Order.DoesNotExist:
            return Response({'error': 'سفارش یافت نشد'}, status=status.HTTP_404_NOT_FOUND)

        price_per_meter = order.project.price_per_meter
        total_refund = float(order.area) * float(price_per_meter)
        penalty = total_refund * 0.005  # 0.5%
        final_refund = total_refund - penalty

        # برگشت پول به اعتبار کاربر
        request.user.credit += final_refund
        request.user.save()

        # ثبت انصراف
        Cancellation.objects.create(
            order=order,
            cancel_price_per_meter=price_per_meter,
            total_refund=final_refund,
            penalty=penalty,
        )

        order.status = 'cancelled'
        order.save()

        return Response({
            'message': 'انصراف با موفقیت ثبت شد',
            'total_refund': final_refund,
            'penalty': penalty,
        })