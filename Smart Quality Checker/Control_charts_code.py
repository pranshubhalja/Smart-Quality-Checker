import pandas as pd
import matplotlib.pyplot as plt

# Load your dataset
df = pd.read_excel('C:/Users/Swara/Desktop/Data_with_Status SQC project.xlsx')

# List of variables you want charts for
variables = [
    "Current_Temperature",
    "Humidity",
    "Steady_State_Error",
    "Ambient_Temperature",
    "Response_Time"
]

def plot_control_chart(df, column_name):
    data = df[column_name]

    mean = data.mean()
    sd = data.std()

    UCL = mean + 3 * sd
    LCL = mean - 3 * sd

    # Identify out-of-control points
    outliers = df[(data > UCL) | (data < LCL)]

    # Plotting
    plt.figure(figsize=(12, 5))
    plt.plot(data.index, data, label="Data")
    plt.axhline(mean, color="black", linestyle="--", label="Mean")
    plt.axhline(UCL, color="red", linestyle="--", label="UCL (+3 SD)")
    plt.axhline(LCL, color="red", linestyle="--", label="LCL (-3 SD)")

    # Highlight outliers
    plt.scatter(outliers.index, outliers[column_name], color="red")
    plt.title(f"Control Chart for {column_name}")
    plt.xlabel("Observation")
    plt.ylabel(column_name)
    plt.legend()
    plt.grid(alpha=0.3)
    plt.show()


# Generate separate charts
for var in variables:
    plot_control_chart(df,var)

