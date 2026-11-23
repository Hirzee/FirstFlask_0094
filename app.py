from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    data_user = None
    error = None

    if request.method == "POST":
        nama = request.form.get("nama", "").strip()
        email = request.form.get("email", "").strip()
        telepon = request.form.get("telepon", "").strip()

        if nama and email and telepon:
            data_user = {
                "nama": nama,
                "email": email,
                "telepon": telepon
            }
        else:
            error = "Semua kolom wajib diisi."

    return render_template("index.html", data=data_user, error=error)

if __name__ == "__main__":
    app.run(debug=True)