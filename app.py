from flask import Flask, render_template

from scraper import get_table_rows

from events_generator import build_events

app = Flask(__name__)


def get_schedule_events():

    rows = get_table_rows()

    events = []

    for row in rows:

        cols = row.find_all("td")

        if len(cols) != 4:
            continue

        date_text = cols[0].get_text("\n", strip=True)

        subject = " ".join(
            cols[1].get_text(" ", strip=True).split()
        )

        classroom = cols[2].get_text(strip=True)

        timing = " ".join(
            cols[3].get_text(" ", strip=True).split()
        )

        events.extend(
            build_events(
                date_text,
                subject,
                classroom,
                timing
            )
        )


    return events


@app.route("/")
def home():

    schedule_error = None

    try:
        events = get_schedule_events()
    except Exception:
        events = []
        schedule_error = (
            "Live EECI schedule could not be loaded. "
            "Your saved custom events are still available."
        )

    return render_template(
        "calendar.html",
        events=events,
        schedule_error=schedule_error
    )


if __name__ == "__main__":
    app.run(debug=True)
