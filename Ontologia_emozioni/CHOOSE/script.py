from collections import Counter
import pandas as pd

# Load and process the contents of the two files
with open("C:\\Users\\39388\\Desktop\\Tesi\\Ontologia_emozioni\\attributi_PRE-SONDAGGIO.txt", "r") as file_marta, open("C:\\Users\\39388\\Desktop\\Tesi\\Ontologia_emozioni\\negate.txt", "r") as file_negate:
    attributes_marta = file_marta.readlines()
    attributes_negate = file_negate.readlines()

# Extract attributes from both files
def extract_attributes(lines):
    attributes = []
    for line in lines:
        line = line.strip()
        if line.startswith("-"):
            attributes.append(line.lstrip("- ").strip())
    return attributes

# Get attributes from both files
marta_attributes = extract_attributes(attributes_marta)
negate_attributes = extract_attributes(attributes_negate)

# Combine attributes and count occurrences
all_attributes = marta_attributes + negate_attributes
attribute_counts = Counter(all_attributes)

# Prepare DataFrame for output
attributes_df = pd.DataFrame(attribute_counts.items(), columns=["Attribute", "Count"])
attributes_df.sort_values(by="Attribute", inplace=True)

# Save the result to an Excel file
combined_attributes_file_path = "C:\\Users\\39388\\Desktop\\Tesi\\Ontologia_emozioni\\combined_attribute_counts.txt"
# attributes_df.to_excel(combined_attributes_file_path, index=False)



with open(combined_attributes_file_path, "w") as txt_file:
    for index, row in attributes_df.iterrows():
        txt_file.write(f"{row['Attribute']}: {row['Count']}\n")