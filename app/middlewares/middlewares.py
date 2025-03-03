import time
from collections import defaultdict
from typing import Dict

from fastapi import Request,Response
from starlette.middleware.base import BaseHTTPMiddleware

from app.config import config

class RequestBaseSetup(BaseHTTPMiddleware):
    def __init__(self, app, dispatch = None):
        super().__init__(app, dispatch)
        self.rate_limit_records = defaultdict(lambda:0.0)

    async def dispatch(self,request:Request,call_next):     # dispatch is a reserved function name of middlewares. 
        response = await call_next(request)
        response.headers["X-custom_header_1"] = "This is a custom header. Welcome to this page. Valar Morghulis."
        client_ip = request.client.host
        current_time = time.time()
        rate_limit = config["RATE_LIMIT_GENERAL"]                   # In seconds.
        limit_check = current_time - self.rate_limit_records[client_ip]
        print("rate_limit : ",rate_limit,"\nlimit_check : ",limit_check)
        if limit_check < rate_limit:
            return Response(content="Too many attempts, Please try again later.",status_code=429)
        self.rate_limit_records[client_ip] = current_time
        return response


# Need to make middlewares for custom APIs.
# Need to include Ratelimitting feature.
