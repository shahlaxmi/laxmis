import pandas as pd
from sklearn.linear_model import LinearRegression 

# Create dataset simple linear regression model
data = {
    "Species": ["Bream","Bream","Bream","Bream","Bream","Bream",
                "Roach","Roach","Roach","Roach","Roach","Roach","Roach"],
    
    "Weight": [242,290,340,363,500,1000,200,180,290,390,160,140,40],
    
    "Length": [25.4,26.3,26.5,29,29.7,37,23.5,25.2,26,31.7,22.5,20.8,14.5]
}

df = pd.DataFrame(data)

# Get unique species
species_list = df["Species"].unique()

print("Simple Linear Regression Results:\n")

for species in species_list:
    
    print(f"----- {species} -----")
    
    # Filter data for each species
    subset = df[df["Species"] == species]
    
    X = subset[["Length"]]   # Independent variable
    y = subset["Weight"]     # Dependent variable
    
    # Create model
    model = LinearRegression()
    model.fit(X, y)
    
    # Get slope & intercept
    slope = model.coef_[0]
    intercept = model.intercept_
    
    print("Slope:", round(slope,2))
    print("Intercept:", round(intercept,2))
    print()
