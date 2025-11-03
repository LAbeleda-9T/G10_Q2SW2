from pyscript import when, document, display

# ✅ Trigger when the calculate button is clicked
@when("click", "#calcBtn")
def calculate_grades(event):
    # --- Student Info ---
    fname = document.getElementById("fname").value.strip()
    lname = document.getElementById("lname").value.strip()

    # --- Subjects and Units ---
    subjects = ["Science", "English", "ICT", "Math", "Filipino", "PE"]
    units = (5, 5, 2, 5, 3, 1)

    # --- Get Grades from Inputs ---
    try:
        grades = [
            float(document.getElementById("sci").value),
            float(document.getElementById("eng").value),
            float(document.getElementById("ict").value),
            float(document.getElementById("math").value),
            float(document.getElementById("fil").value),
            float(document.getElementById("pe").value)
        ]
    except ValueError:
        display("⚠️ Please enter a valid  grades for all subjects.", target="output", append=False)
        return

    # --- Compute GWA ---
    total_units = sum(units)
    weighted_sum = sum(g * u for g, u in zip(grades, units))
    gwa = weighted_sum / total_units

    # --- Clear previous output ---
    document.getElementById("output").innerText = ""

    # --- Build output message ---
    message = f"""
👩🏻‍🎓Student Information

Name: {fname} {lname}

🏆 Summary of Grades
{''.join(f"{subj}: {grade:.2f}\n" for subj, grade in zip(subjects, grades))}

📊 General Weighted Average (GWA): {gwa:.2f}
"""

    # --- Display output ---
    display(message, target="output")
