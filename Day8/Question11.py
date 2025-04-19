from flask import Flask, request, Response, jsonify
import random

app = Flask(__name__)

@app.route("/weather/<city>", methods=["GET"])
def weather(city):
    format_type = request.args.get("format")  
    temp = f"{random.randint(20, 40)}°C"      

    if format_type == "xml":
        xml_data = f"""
        <weather>
            <city>{city}</city>
            <temperature>{temp}</temperature>
            <unit>Celsius</unit>
        </weather>
        """
        return Response(xml_data.strip())
    
    # Default JSON response
    json_data = {
        "city": city,
        "temperature": temp,
        "unit": "Celsius"
    }
    return jsonify(json_data)

if __name__ == "__main__":
    app.run(debug=True)
