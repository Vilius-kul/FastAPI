import datetime
import uuid

from models.location import Location
from models.reports import Report

__reports: list[Report] = []


async def get_reports() -> list:
    # Would be an async call here.
    return list(__reports)


async def add_report(description: str, location: Location) -> object:
    now = datetime.datetime.now()
    report = Report(
        id=str(uuid.uuid4()),
        description=description,
        location=location,
        created_date=now,
    )

    # Simulate saving to the DB
    # Would be an async call here.
    __reports.append(report)

    __reports.sort(key=lambda r: r.created_date, reverse=True)  # type: ignore

    return report
