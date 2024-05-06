import math
from scipy.optimize import minimize

# Constants for cooling calculations
initial_temperature_beer = 24  # °C
desired_temperature_beer = 13  # °C
refrigerator_temperature = 4  # °C
specific_heat_beer = 4.18  # kJ/kg°C
specific_heat_steel = 0.502  # kJ/kg°C
heat_transfer_coefficient_air = 20  # W/m²°C (approximate)
density_beer = 1000  # kg/m^3
density_stainless_steel = 7850  # kg/m^3

# Specific stainless steel properties
body_thickness = 2.0e-3  # m
chimb_thickness = 2.5e-3  # m
neck_thickness = 2.0e-3  # m

# Function to calculate the mass of a single keg
def calculate_keg_mass(d, h):
    """Calculates the mass of a keg based on diameter and height."""
    r = d / 2
    body_area = 2 * math.pi * r * h
    chimb_area = 2 * math.pi * r**2
    neck_area = math.pi * r**2

    mass_body = body_area * body_thickness * density_stainless_steel
    mass_chimb = chimb_area * chimb_thickness * density_stainless_steel
    mass_neck = neck_area * neck_thickness * density_stainless_steel
    
    return mass_body + mass_chimb + mass_neck

# Function to calculate the cooling energy required for a keg
def calculate_cooling_energy(mass_beer, mass_keg):
    """Calculates the cooling energy required to cool a keg from initial to desired temperature."""
    energy_beer = mass_beer * specific_heat_beer * (initial_temperature_beer - desired_temperature_beer)
    energy_keg = mass_keg * specific_heat_steel * (initial_temperature_beer - desired_temperature_beer)
    return energy_beer + energy_keg

# Function to calculate the cooling time using Newton's Law of Cooling
def calculate_cooling_time(surface_area, mass_beer, mass_keg, initial_temperature_beer, desired_temperature_beer, refrigerator_temperature, heat_transfer_coefficient_air):
    """Calculates the time required to cool the kegs using Newton's Law of Cooling."""
    total_mass = mass_beer + mass_keg
    specific_heat_total = (mass_beer * specific_heat_beer + mass_keg * specific_heat_steel) / total_mass
    k = (heat_transfer_coefficient_air * surface_area) / (total_mass * specific_heat_total)
    
    t = (-1 / k) * math.log((desired_temperature_beer - refrigerator_temperature) / (initial_temperature_beer - refrigerator_temperature))
    return t

# Optimization function with keg material ratio
def optimize_keg_size_with_cooling(l_fridge, w_fridge, h_fridge, spacing=0.05):
    """Optimizes keg size and number for given refrigeration space considering cooling requirements."""
    v_fridge = l_fridge * w_fridge * h_fridge  # Total refrigerator volume (m^3)
    k = 2.0  # Assume height-to-diameter ratio
    keg_material_to_liquid_ratio = 0.1  # 10% of keg is material, 90% is liquid
    
    # Optimization function to maximize surface area
    def objective(x):
        d = x[0]
        d_with_spacing = d + spacing
        h = k * d
        h_with_spacing = h + spacing
        v_keg = (math.pi * d**2 * h) / 4
        v_liquid = v_keg * (1 - keg_material_to_liquid_ratio)
        a_keg = (math.pi * d**2) / 2 * (1 + 2 * k)
        
        n_kegs = math.floor(l_fridge / d_with_spacing) * math.floor(w_fridge / d_with_spacing) * math.floor(h_fridge / h_with_spacing)
        total_area = n_kegs * a_keg
        return -total_area  # Negative for maximization
    
    # Volume constraint ensuring the total volume does not exceed refrigerator capacity
    def volume_constraint(x):
        d = x[0]
        d_with_spacing = d + spacing
        h = k * d
        h_with_spacing = h + spacing
        v_keg = (math.pi * d**2 * h) / 4
        n_kegs = math.floor(l_fridge / d_with_spacing) * math.floor(w_fridge / d_with_spacing) * math.floor(h_fridge / h_with_spacing)
        total_volume = n_kegs * v_keg
        return v_fridge - total_volume
    
    # Initial guess for keg diameter
    x0 = [0.3]
    
    # Optimization bounds and constraints
    bounds = [(0.1, l_fridge)]
    constraints = [{'type': 'ineq', 'fun': volume_constraint}]
    
    # Optimize
    result = minimize(objective, x0, method='SLSQP', bounds=bounds, constraints=constraints)
    
    # Results
    optimal_d = result.x[0]
    optimal_h = k * optimal_d
    optimal_d_with_spacing = optimal_d + spacing
    optimal_h_with_spacing = optimal_h + spacing
    optimal_v_keg = (math.pi * optimal_d**2 * optimal_h) / 4
    optimal_v_liquid = optimal_v_keg * (1 - keg_material_to_liquid_ratio)
    optimal_v_material = optimal_v_keg * keg_material_to_liquid_ratio
    optimal_a_keg = (math.pi * optimal_d**2) / 2 * (1 + 2 * k)
    optimal_n_kegs = math.floor(l_fridge / optimal_d_with_spacing) * math.floor(w_fridge / optimal_d_with_spacing) * math.floor(h_fridge / optimal_h_with_spacing)
    
    total_volume = optimal_n_kegs * optimal_v_keg
    total_volume_liquid = optimal_n_kegs * optimal_v_liquid
    total_volume_material = optimal_n_kegs * optimal_v_material
    total_surface_area = optimal_n_kegs * optimal_a_keg
    total_mass_kegs = sum([calculate_keg_mass(optimal_d, optimal_h) for _ in range(optimal_n_kegs)])
    total_mass_liquid = total_volume_liquid * density_beer
    total_mass = total_mass_liquid + total_mass_kegs
    total_cooling_energy = calculate_cooling_energy(total_mass_liquid, total_mass_kegs)
    total_cooling_time = calculate_cooling_time(total_surface_area, total_mass_liquid, total_mass_kegs, initial_temperature_beer, desired_temperature_beer, refrigerator_temperature, heat_transfer_coefficient_air)
    
    return {
        "Fridge Dimensions": (l_fridge, w_fridge, h_fridge),
        "Optimal Keg Diameter": optimal_d,
        "Optimal Keg Height": optimal_h,
        "Optimal Number of Kegs": optimal_n_kegs,
        "Total Volume of Beer (Including Keg Material)": total_volume,
        "Total Volume of Liquid": total_volume_liquid,
        "Total Volume of Material": total_volume_material,
        "Total Surface Area": total_surface_area,
        "Beer per Keg": optimal_v_liquid,
        "Total Mass of Liquid (kg)": total_mass_liquid,
        "Total Mass of Kegs (kg)": total_mass_kegs,
        "Total Mass (kg)": total_mass,
        "Total Cooling Energy (kJ)": total_cooling_energy,
        "Total Cooling Time (s)": total_cooling_time
    }

# Running optimizations with 5 room sizes considering cooling requirements
results_with_cooling = [
    optimize_keg_size_with_cooling(5, 5, 5),
    optimize_keg_size_with_cooling(10, 10, 10),
    optimize_keg_size_with_cooling(20, 20, 20),
    optimize_keg_size_with_cooling(30, 30, 30),
    optimize_keg_size_with_cooling(40, 40, 40)
]

results_with_cooling
