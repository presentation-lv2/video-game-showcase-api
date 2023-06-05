"""
URL configuration for gameproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from gameapp.routers import GameRouter, TargetRouter, GameTargetRouter,UsersRouter, CategoryRouter, GameCategoryRouter, PostRouter
from gameapp.views import SwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(GameRouter.router.urls)),
    path('', include(TargetRouter.router.urls)),
    path('', include(GameTargetRouter.router.urls)),
    path('', include(UsersRouter.router.urls)),
    path('', include(CategoryRouter.router.urls)),
    path('', include(GameCategoryRouter.router.urls)),
    path('', include(PostRouter.router.urls)),
    path('api/swagger/', SwaggerView.schema_view.with_ui("swagger", cache_timeout=0))
]
