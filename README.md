## Problem Statement

Given various refrigeration unit sizes, determine the optimal keg size and number of kegs that maximize surface area while ensuring efficient cooling.



### Assumptions

- Initial Temperature of Beer: 24°C

- Desired Temperature of Beer: 13°C

- Refrigerator Temperature: 4°C

- Heat Transfer Coefficient (Air): 20 W/m²°C

- Specific Heat Capacity of Beer: 4.18 kJ/kg°C

- Specific Heat Capacity of Stainless Steel (AISI 304): 0.502 kJ/kg°C

- Density of Beer: 1000 kg/m³

- Density of Stainless Steel (AISI 304): 7850 kg/m³



## Results and Analysis



### Optimized Results with Cooling Requirements



1. **5m x 5m x 5m (125 m³)**

   - **Optimal Keg Diameter:** 0.307 m

   - **Optimal Keg Height:** 0.614 m

   - **Optimal Number of Kegs:** 1,372

   - **Total Volume of Beer (Including Keg Material):** 62.44 m³

   - **Total Volume of Liquid:** 56.20 m³

   - **Total Volume of Material:** 6.24 m³

   - **Total Surface Area:** 1,016.54 m²

   - **Beer per Keg:** 0.041 m³ (41 L)

   - **Total Mass of Liquid (Beer):** 56,200.05 kg

   - **Total Mass of Kegs (Stainless Steel):** 18,353.61 kg

   - **Total Mass:** 74,553.66 kg

   - **Total Cooling Energy (kJ):** 2,685,426.73 kJ

   - **Total Cooling Time (s):** 9,588.39 s (2.66 h)



2. **10m x 10m x 10m (1,000 m³)**

   - **Optimal Keg Diameter:** 0.307 m

   - **Optimal Keg Height:** 0.614 m

   - **Optimal Number of Kegs:** 11,760

   - **Total Volume of Beer (Including Keg Material):** 535.24 m³

   - **Total Volume of Liquid:** 481.72 m³

   - **Total Volume of Material:** 53.52 m³

   - **Total Surface Area:** 8,713.21 m²

   - **Beer per Keg:** 0.041 m³ (41 L)

   - **Total Mass of Liquid (Beer):** 481,715.87 kg

   - **Total Mass of Kegs (Stainless Steel):** 157,316.95 kg

   - **Total Mass:** 639,032.83 kg

   - **Total Cooling Energy (kJ):** 23,018,000.14 kJ

   - **Total Cooling Time (s):** 9,588.40 s (2.66 h)



3. **20m x 20m x 20m (8,000 m³)**

   - **Optimal Keg Diameter:** 0.300 m

   - **Optimal Keg Height:** 0.600 m

   - **Optimal Number of Kegs:** 97,470

   - **Total Volume of Beer (Including Keg Material):** 4,133.85 m³

   - **Total Volume of Liquid:** 3,720.46 m³

   - **Total Volume of Material:** 413.38 m³

   - **Total Surface Area:** 68,897.48 m²

   - **Beer per Keg:** 0.038 m³ (38 L)

   - **Total Mass of Liquid (Beer):** 3,720,464.09 kg

   - **Total Mass of Kegs (Stainless Steel):** 1,243,944.06 kg

   - **Total Mass:** 4,964,408.14 kg

   - **Total Cooling Energy (kJ):** 177,935,997.79 kJ

   - **Total Cooling Time (s):** 9,373.83 s (2.60 h)



4. **30m x 30m x 30m (27,000 m³)**

   - **Optimal Keg Diameter:** 0.311 m

   - **Optimal Keg Height:** 0.623 m

   - **Optimal Number of Kegs:** 303,116

   - **Total Volume of Beer (Including Keg Material):** 14,383.87 m³

   - **Total Volume of Liquid:** 12,945.48 m³

   - **Total Volume of Material:** 1,438.39 m³

   - **Total Surface Area:** 230,920.96 m²

   - **Beer per Keg:** 0.043 m³ (43 L)

   - **Total Mass of Liquid (Beer):** 12,945,479.97 kg

   - **Total Mass of Kegs (Stainless Steel):** 4,169,277.88 kg

   - **Total Mass:** 17,114,757.85 kg

   - **Total Cooling Energy (kJ):** 618,255,921.52 kJ

   - **Total Cooling Time (s):** 9,717.65 s (2.70 h)



5. **40m x 40m x 40m (64,000 m³)**

   - **Optimal Keg Diameter:** 0.300 m

   - **Optimal Keg Height:** 0.600 m

   - **Optimal Number of Kegs:** 792,756

   - **Total Volume of Beer (Including Keg Material):** 33,621.97 m³

   - **Total Volume of Liquid:** 30,259.77 m³

   - **Total Volume of Material:** 3,362.20 m³

   - **Total Surface Area:** 560,366.20 m²

   - **Beer per Keg:** 0.038 m³ (38 L)

   - **Total Mass of Liquid (Beer):** 30,259,774.57 kg

   - **Total Mass of Kegs (Stainless Steel):** 10,117,411.66 kg

   - **Total Mass:** 40,377,186.24 kg

   - **Total Cooling Energy (kJ):** 1,447,212,782.04 kJ

   - **Total Cooling Time (s):** 9,373.83 s (2.60 h)



### Observed Trends

1. **Keg Size Consistency:**

   - The optimal keg diameter and height are consistent across different refrigeration sizes:

     - **Diameter:** Around 0.300 m to 0.311 m

     - **Height:** Around 0.600 m to 0.623 m



2. **Cooling Energy Requirements:**

   - The cooling energy requirement scales exponentially with the refrigerator size.

   - For instance, a 5m x 5m x 5m space requires about 2.69 million kJ, while a 40m x 40m x 40m space requires 1.45 billion kJ.



3. **Cooling Time Consistency:**

   - The cooling time remains relatively consistent across different refrigeration sizes, ranging from 9,373 s to 9,717 s (around 2.6 to 2.7 hours).



### Analysis Conclusion

1. **Optimal Keg Size Selection:**

   - The keg diameter should generally be around 0.300 m to 0.311 m, and the height around 0.600 m to 0.623 m.



2. **Cooling Time Insight:**

   - Despite the significant differences in total mass and energy requirements across room sizes, the consistent cooling times indicate that heat transfer efficiency is crucial.

   - Ensuring proper airflow, refrigeration power, and heat transfer coefficient is essential for consistent cooling.



## References

- Stainless Steel Properties: [AISI 304 Steel](https://en.wikipedia.org/wiki/SAE_304_stainless_steel)

- Newton's Law of Cooling: [Wikipedia Article](https://en.wikipedia.org/wiki/Newton%27s_law_of_cooling)

"""
