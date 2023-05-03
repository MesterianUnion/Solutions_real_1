from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy import extract

import topbike_data as tpd
import topbike_sql as tpsql

def booked_bane(bane, date_):
    with Session(tpsql.engine) as session:
        records = session.scalars(select(tpd.Bookings).where(tpd.Bookings.bane_id == bane.id).where(extract("day", tpd.Bookings.date) == date_.day).where(extract("month", tpd.Bookings.date) == date_.month).where(extract("year", tpd.Bookings.date) == date_.year))
        weight = 0
        for record in records:
            weight += tpsql.get_record(tpd.Hold, record.id).hold_size

    print(weight)
    return weight


def capacity_available(bane, date_, new_hold):
    booked = booked_bane(bane, date_)

    return bane.max_capacity >= booked + new_hold.hold_size