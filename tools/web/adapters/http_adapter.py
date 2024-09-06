

def http_adapter(request, controller, **kwargs):
    response = controller.execute(request, data=kwargs["input"], response=kwargs["response"])
    return response