from pydantic import BaseModel, constr, confloat


class TicketReqVal(BaseModel):
    id: str
    title = constr(min_length=5, max_length=50)
    price = confloat(gt=0)
    user_id = str
    version = int
