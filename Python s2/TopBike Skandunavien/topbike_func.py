from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy import extract

import topbike_data as tpd
import topbike_sql as tpsql


def booked_bane(bane_id, date_):
    with Session(tpsql.engine) as session:
        records = session.scalars(select(tpd.Bookings).where(tpd.Bookings.bane_id == bane_id.id).where(extract("day", tpd.Bookings.dato) == date_.day).where(extract("month", tpd.Bookings.dato) == date_.month).where(extract("year", tpd.Bookings.dato) == date_.year))
    length=0
    for r in records:
        length+=1
    print(length)

    return length > 0


def capacity_available(bane_id, date_, new_hold):
    booked = booked_bane(bane_id, date_)

    return bane_id.kapacitet >= booked + new_hold.storelse