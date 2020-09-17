from pydantic import BaseModel, constr, confloat


class TicketReqVal(BaseModel):
    title: constr(min_length=5, max_length=50)
    price: confloat(gt=0)

    class Config:
        extra = 'forbid'
