# src/report.py

def generate_report(
        recommendations):

    with open(
            "outputs/report.txt",
            "w") as file:

        file.write(
            "Recommended Products\n"
        )

        for item in recommendations:

            file.write(
                f"{item['name']}\n"
            )