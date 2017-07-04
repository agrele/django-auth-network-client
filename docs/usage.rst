=====
Usage
=====

To use Django Auth Network Client in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_auth_network_client.apps.DjangoAuthNetworkClientConfig',
        ...
    )

Add Django Auth Network Client's URL patterns:

.. code-block:: python

    from django_auth_network_client import urls as django_auth_network_client_urls


    urlpatterns = [
        ...
        url(r'^', include(django_auth_network_client_urls)),
        ...
    ]
