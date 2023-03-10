from fastapi import APIRouter, Request, Response, Depends


class CreditCardRouter:

    __router = APIRouter(prefix="/api/v1", tags=["Credit Card"])

    @staticmethod
    def get_credit_card_router():
        return CreditCardRouter.__router

    @staticmethod
    @__router.get("/credit-card")
    async def get_all_credit_cards(request: Request):
        pass

    @staticmethod
    @__router.get("/credit-card/<:key>")
    async def get_one_credit_card(request: Request, payload: CreditCardValidator):
        pass

    @staticmethod
    @__router.post("/credit-card")
    async def register_new_credit_card(request: Request, payload: CreditCardValidator = Depends()):
        pass







