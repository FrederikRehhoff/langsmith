# import pandas as pd
# import ast  # For converting string representations of lists to actual lists

# def compare_files_with_complete_handling(text_file_path, excel_file_path, output_file_path):
#     # Load and process the text file
#     with open(text_file_path, 'r') as file:
#         text_lines = file.readlines()
#     text_data = pd.DataFrame([line.strip().split(';') for line in text_lines],
#                              columns=['Robot', 'Tool', 'Item', 'Location'])

#     # Load and process the Excel file
#     excel_data = pd.read_excel(excel_file_path, header=None)
    
#     # Handle lists in the Robot and Tool columns directly in the main dataset
#     excel_data[1] = excel_data[1].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) and x.startswith('[') else [x])
#     excel_data[2] = excel_data[2].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) and x.startswith('[') else [x])

#     # Extract and flatten lists of alternative robots and tools
#     excel_data['Alt Robots'] = excel_data[5].apply(lambda x: [item for sublist in ast.literal_eval(x) for item in sublist])
#     excel_data['Alt Tools'] = excel_data[6].apply(lambda x: ast.literal_eval(x))

#     # Compare the data for main robots and tools
#     comparison_results_robots = text_data['Robot'].apply(lambda x: any(x in sublist for sublist in excel_data[1]))
#     comparison_results_tools = text_data['Tool'].apply(lambda x: any(x in sublist for sublist in excel_data[2]))

#     # Check for alternative robots and tools
#     boolean_data = excel_data[[0]].copy()  # Copy the description column
#     boolean_data['Robot'] = comparison_results_robots
#     boolean_data['Tool'] = comparison_results_tools
#     boolean_data['Item'] = excel_data[3] == text_data['Item']
#     boolean_data['Location'] = excel_data[4] == text_data['Location']
#     boolean_data['Alt Robot'] = text_data['Robot'].apply(lambda x: x in excel_data['Alt Robots'].explode().unique())
#     boolean_data['Alt Tool'] = text_data['Tool'].apply(lambda x: any(x in sublist for sublist in excel_data['Alt Tools']))

#     # Save the DataFrame with boolean values to a new Excel file
#     boolean_data.to_excel(output_file_path, index=False)
# Load the Excel file directly (now properly formatted)
    

import pandas as pd
import ast

def compare_files_with_complete_handling(text_file_path, excel_file_path, output_file_path):
    # Load and process the text file
    with open(text_file_path, 'r') as file:
        text_data = pd.DataFrame([line.strip().split(';') for line in file.readlines()],
                                 columns=['Robot', 'Tool', 'Item', 'Location'])

    # Load the Excel file directly (now properly formatted)
    excel_data = pd.read_excel(excel_file_path, header=None)
    excel_data.columns = ['Description', 'Robot', 'Tool', 'Item', 'Location', 'Alt Robots', 'Alt Tools']
    
    # Convert string representations of lists to actual lists using ast.literal_eval
    excel_data['Robot'] = excel_data['Robot'].apply(lambda x: ast.literal_eval(x))
    excel_data['Tool'] = excel_data['Tool'].apply(lambda x: ast.literal_eval(x))
    excel_data['Alt Robots'] = excel_data['Alt Robots'].apply(lambda x: [item for sublist in ast.literal_eval(x) for item in sublist])
    excel_data['Alt Tools'] = excel_data['Alt Tools'].apply(lambda x: ast.literal_eval(x))

    # Ensure both data sets have the same length
    if len(text_data) != len(excel_data):
        raise ValueError("The number of rows in text data and Excel data do not match.")

    # Compare each row in text_data against the corresponding row in excel_data
    results = pd.DataFrame({
        'Description': excel_data['Description'],
        'Robot': [compare_primary(excel_data.at[i, 'Robot'], text_data.at[i, 'Robot']) for i in range(len(text_data))],
        'Tool': [compare_primary(excel_data.at[i, 'Tool'], text_data.at[i, 'Tool']) for i in range(len(text_data))],
        'Item': [excel_data.at[i, 'Item'] == text_data.at[i, 'Item'] for i in range(len(text_data))],
        'Location': [excel_data.at[i, 'Location'] == text_data.at[i, 'Location'] for i in range(len(text_data))],
        'Alt Robot': [compare_primary(excel_data.at[i, 'Alt Robots'], text_data.at[i, 'Robot']) for i in range(len(text_data))],
        'Alt Tool': [compare_primary(excel_data.at[i, 'Alt Tools'], text_data.at[i, 'Tool']) for i in range(len(text_data))],
    })

    # Save the DataFrame with boolean values to a new Excel file
    results.to_excel(output_file_path, index=False)

# Helper function to compare primary data
def compare_primary(excel_list, text_value):
    return text_value in excel_list

# Usage of the function
# compare_files_with_complete_handling('path_to_text_file.txt', 'path_to_excel_file.xlsx', 'output_file.xlsx')




    

##### ReAct Comparison #####

# File paths for the text and Excel files
text_file_path = 'Results\Result_matrix\Easy_react_matrix.txt'
excel_file_path = 'Results\Easy_task_validation.xlsx'
output_file_path = 'Results\comparison_results\Easy_comparison\Easy_react_comparison_Results.xlsx'

# Run the function
compare_files_with_complete_handling(text_file_path, excel_file_path, output_file_path)

# Paths for the files (update these paths according to your file locations)
text_file_path = 'Results\Result_matrix\Medium_react_matrix.txt'
excel_file_path = 'Results\Medium_task_validation.xlsx'
output_file_path = 'Results\comparison_results\Medium_comparison\Medium_react_comparison_Results.xlsx'

# Run the function
compare_files_with_complete_handling(text_file_path, excel_file_path, output_file_path)

# File paths for the text and Excel files
text_file_path = 'Results\Result_matrix\Hard_react_matrix.txt'
excel_file_path = 'Results\Hard_task_validation.xlsx'
output_file_path = 'Results\comparison_results\Hard_comparison\Hard_react_comparison_Results.xlsx'

# Run the function
compare_files_with_complete_handling(text_file_path, excel_file_path, output_file_path)


##### Normal Comparison #####

# File paths for the text and Excel files
text_file_path = 'Results\Result_matrix\Easy_matrix.txt'
excel_file_path = 'Results\Easy_task_validation.xlsx'
output_file_path = 'Results\comparison_results\Easy_comparison\Easy_normal_comparison_Results.xlsx'

# Run the function
compare_files_with_complete_handling(text_file_path, excel_file_path, output_file_path)

# Paths for the files (update these paths according to your file locations)
text_file_path = 'Results\Result_matrix\Medium_matrix.txt'
excel_file_path = 'Results\Medium_task_validation.xlsx'
output_file_path = 'Results\comparison_results\Medium_comparison\Medium_normal_comparison_Results.xlsx'

# Run the function
compare_files_with_complete_handling(text_file_path, excel_file_path, output_file_path)

# File paths for the text and Excel files
text_file_path = 'Results\Result_matrix\Hard_matrix.txt'
excel_file_path = 'Results\Hard_task_validation.xlsx'
output_file_path = 'Results\comparison_results\Hard_comparison\Hard_normal_comparison_Results.xlsx'

# Run the function
compare_files_with_complete_handling(text_file_path, excel_file_path, output_file_path)