from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings
admin.autodiscover()
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),
    (r'^admin/', include(admin.site.urls)),
    
    (r'^$','MSE_Alumni.views.home'),
    
    #(r'^sign_in/','MSE_Alumni.views.signin'),  
    (r'^sign_out/', 'MSE_Alumni.views.signout'),
    
    (r'^register/', 'MSE_Alumni.views.register'),
    (r'^education_view/', 'MSE_Alumni.views.education_view'),
    (r'^education_add/', 'MSE_Alumni.views.education_add'),
    (r'^education_update/', 'MSE_Alumni.views.education_update'),
    (r'^working_view/', 'MSE_Alumni.views.working_view'),
    (r'^working_add/', 'MSE_Alumni.views.working_add'),
    (r'^working_update/', 'MSE_Alumni.views.working_update'),
    (r'^search/', 'MSE_Alumni.views.search'),
    
    (r'^admin_search/', 'MSE_Alumni.views.admin_search'),
    (r'^admin_comfirm/', 'MSE_Alumni.views.admin_comfirmregistration'),
    (r'^admin_groups/', 'MSE_Alumni.views.admin_groups'),
    (r'^admin_mail_message/', 'MSE_Alumni.views.admin_mail_message'),
    (r'^admin_message/$', 'MSE_Alumni.views.admin_message'),
    (r'^admin_alumniprofile/$', 'MSE_Alumni.views.admin_view_profile'),
    
    (r'^ajax_signin/$', 'MSE_Alumni.views.ajax_signin'),
    (r'^ajax_register/$', 'MSE_Alumni.views.ajax_register'),  
    # Examples:
    # url(r'^$', 'Alumni.views.home', name='home'),
    # url(r'^Alumni/', include('Alumni.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
