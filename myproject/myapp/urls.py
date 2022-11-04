from django.urls import path, include
from.import views
#. は今いるところ（myappの中）って言う意味。

app_name="myapp"

urlpatterns = [
    path("", views.Index.as_view(),name="index"),
    path('post_create',views.PostCreate.as_view(), name='post_page'),
    path('post_detail/<int:pk>',views.PostDetail.as_view(), name='post_detail'),
    path('post_update/<int:pk>',views.PostUpdate.as_view(), name='post_update'),
    path('post_delete/<int:pk>',views.PostDelete.as_view(), name='post_delete'),

    # 道のりに名前を付ける作業がpath。
    # 道のりが長すぎると　A/B/C/D/E/目的のファイル　みたいに複雑になるから、簡易的な名前付けてやりやすくするってこと。
]
#viewsに行ってIndexっていう関数を参照しろよってこと
# .as_view() は、見方を変えろよってこと