from pydantic import BaseModel


class OrderReqVal(BaseModel):
    ticket_id: str

    class Config:
        extra = 'forbid'
