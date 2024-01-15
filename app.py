import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of your app
st.title('Public Health Insights App')

# Introduction
st.write('Explore public health data in India')

# Load your datasets
covid_data = pd.read_csv('C:\\Users\\user\\Downloads\\1.csv', encoding='utf-8')
sanitation_data = pd.read_csv('C:\\Users\\user\\Downloads\\2.csv', encoding='utf-8')
poverty_data = pd.read_csv('C:\\Users\\user\\Downloads\\3.csv', encoding='utf-8')
violence_data = pd.read_csv('C:\\Users\\user\\Downloads\\4.csv', encoding='utf-8')
environment_data = pd.read_csv('C:\\Users\\user\\Downloads\\5.csv', encoding='utf-8')
convicts_data = pd.read_csv('C:\\Users\\user\\Downloads\\6.csv', encoding='utf-8')

# Sidebar Filters
st.sidebar.title('Filters')

# Check if 'State/UT' column exists in the dataset
if 'STATE/UT' in convicts_data.columns:
    # Allow selection of multiple states
    selected_states = st.sidebar.multiselect('Select State/UT:', convicts_data['STATE/UT'].unique())
else:
    selected_states = None

# Check if 'Year' column exists in the dataset
if 'YEAR' in convicts_data.columns:
    selected_year = st.sidebar.slider('Select Year:', min_value=int(convicts_data['YEAR'].min()), max_value=int(convicts_data['YEAR'].max()), value=int(convicts_data['YEAR'].max()))
else:
    selected_year = None

# Main Content
st.sidebar.write('### Data Samples')
st.sidebar.write('Sample of COVID-19 Testing Data:')
st.sidebar.write(covid_data.head())

st.sidebar.write('Sample of Sanitation Data:')
st.sidebar.write(sanitation_data.head())

st.sidebar.write('Sample of Poverty Data:')
st.sidebar.write(poverty_data.head())

st.sidebar.write('Sample of Violence Data:')
st.sidebar.write(violence_data.head())

st.sidebar.write('Sample of Environment Data:')
st.sidebar.write(environment_data.head())

st.sidebar.write('Sample of Convicts Data:')
st.sidebar.write(convicts_data.head())

# Main Content - Bar Charts
st.write('## Bar Charts')

# Bar chart for COVID-19 Testing Data
st.write('### COVID-19 Testing Data')
st.bar_chart(covid_data.set_index('State'))

# Bar chart for Sanitation Data
st.write('### Sanitation Data')
sanitation_data_chart = sanitation_data[['StateName', 'IHHLCoveragePer']] if 'sanitation_data' in locals() else None
if sanitation_data_chart is not None:
    st.bar_chart(sanitation_data_chart.set_index('StateName'))
else:
    st.write('Sanitation data not available.')

# Bar chart for Poverty Data
st.write('### Poverty Data')
poverty_data_chart = poverty_data[['States/Uts', 'Total - No. of Persons (lakhs)']] if 'poverty_data' in locals() else None
if poverty_data_chart is not None:
    st.bar_chart(poverty_data_chart.set_index('States/Uts'))
else:
    st.write('Poverty data not available.')

# Bar chart for Violence Data
st.write('### Violence Data')
violence_data_chart = violence_data[['SL', 'No. of Incidents/Attacks - Total Incidents of Attacks']] if 'violence_data' in locals() else None
if violence_data_chart is not None:
    st.bar_chart(violence_data_chart.set_index('SL'))
else:
    st.write('Violence data not available.')

# Bar chart for Environment Data
st.write('### Environment Data')
if 'environment_data' in locals() and environment_data is not None and not environment_data.empty:
    selected_column = st.selectbox('Select a column for visualization:', environment_data.columns)
    if selected_column:
        try:
            environment_data[selected_column] = pd.to_numeric(environment_data[selected_column])
            st.bar_chart(environment_data[selected_column])
        except:
            st.write(f"Could not visualize {selected_column}. Please select another column.")
else:
    st.write('Environment data not available.')

# Bar chart for Convicts Data
st.write('### Convicts Data')
if selected_states is not None and selected_year is not None:
    filtered_convicts_data = convicts_data[(convicts_data['STATE/UT'].isin(selected_states)) & (convicts_data['YEAR'] == selected_year)]
    st.write(f"### Filtered Convicts Data for {', '.join(selected_states)} in {selected_year}")
    st.write(filtered_convicts_data)

    # Display descriptive statistics
    st.write(f"### Descriptive Statistics for Convicts Data in {', '.join(selected_states)} in {selected_year}")
    st.write(filtered_convicts_data.describe())

    # Bar chart for Convicts Data
    st.write('### Convicts Data')
    if not filtered_convicts_data.empty:
        selected_column_convicts = st.selectbox('Select a column for visualization:', filtered_convicts_data.columns)
        if selected_column_convicts:
            try:
                filtered_convicts_data[selected_column_convicts] = pd.to_numeric(filtered_convicts_data[selected_column_convicts])
                st.bar_chart(filtered_convicts_data[selected_column_convicts])
            except:
                st.write(f"Could not visualize {selected_column_convicts}. Please select another column.")
    else:
        st.write('Convicts data not available.')
else:
    st.write('Please select both State/UT and Year.')

# Main Content - Line Charts
st.write('## Line Charts')

# Line chart for COVID-19 Testing Data
st.write('### COVID-19 Testing Data')
if 'Year' in covid_data.columns:
    st.line_chart(covid_data.groupby('Year').sum()[['Total Samples Tested', 'Total Individuals Tested']])
else:
    st.write('Year column not found in COVID-19 Testing Data.')

# Line chart for Sanitation Data
st.write('### Sanitation Data')
if 'Year' in sanitation_data.columns:
    st.line_chart(sanitation_data.groupby('Year').mean()['IHHLCoveragePer'])
else:
    st.write('Year column not found in Sanitation Data.')

# Line chart for Poverty Data
st.write('### Poverty Data')
if 'Year' in poverty_data.columns:
    st.line_chart(poverty_data.groupby('Year').sum()['Total - No. of Persons (lakhs)'])
else:
    st.write('Year column not found in Poverty Data.')

# Line chart for Violence Data
st.write('### Violence Data')
if 'Year' in violence_data.columns:
    st.line_chart(violence_data.groupby('Year').sum()['No. of Incidents/Attacks - Total Incidents of Attacks'])
else:
    st.write('Year column not found in Violence Data.')

# Line chart for Environment Data
st.write('### Environment Data')
if 'Year' in environment_data.columns:
    selected_column_env = st.selectbox('Select a column for visualization:', environment_data.columns)
    if selected_column_env:
        try:
            environment_data[selected_column_env] = pd.to_numeric(environment_data[selected_column_env])
            st.line_chart(environment_data.groupby('Year').mean()[selected_column_env])
        except:
            st.write(f"Could not visualize {selected_column_env}. Please select another column.")
    else:
        st.write('Please select a column for visualization.')
else:
    st.write('Year column not found in Environment Data.')

# Line chart for Convicts Data
st.write('### Convicts Data')
if selected_states is not None:
    if 'Year' in convicts_data.columns:
        selected_column_line = st.selectbox('Select a column for line chart:', convicts_data.columns)
        if selected_column_line:
            filtered_convicts_data_line = convicts_data[convicts_data['STATE/UT'].isin(selected_states)].groupby('Year').sum()[selected_column_line]
            st.line_chart(filtered_convicts_data_line)
        else:
            st.write('Please select a column for the line chart.')
    else:
        st.write('Year column not found in Convicts Data.')

# Main Content - Pie Charts
st.write('## Pie Charts')

# Pie chart for Convicts Data
st.write('### Convicts Data')
if selected_states is not None:
    filtered_convicts_data_pie = convicts_data[convicts_data['STATE/UT'].isin(selected_states)].iloc[:, 3:15]

    # Check if the DataFrame is not empty
    if not filtered_convicts_data_pie.empty:
        # Replace NaN values with 0
        filtered_convicts_data_pie.fillna(0, inplace=True)

        # Plot pie chart using Matplotlib
        fig, ax = plt.subplots()
        ax.pie(filtered_convicts_data_pie.iloc[0], labels=filtered_convicts_data_pie.columns, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        # Display the pie chart using Streamlit
        st.pyplot(fig)
    else:
        st.write('No data available for the selected State/UT.')
else:
    st.write('Please select a State/UT.')


# Main Content - Maps and Other Charts
st.write('## Maps and Other Charts')

# Map showing Convicts Data
st.write('### Map Showing Convicts Data')
if 'Latitude' in convicts_data.columns and 'Longitude' in convicts_data.columns:
    if selected_states and selected_states[0] in convicts_data['STATE/UT'].unique():
        st.map(convicts_data[convicts_data['STATE/UT'] == selected_states[0]][['Latitude', 'Longitude']])
    else:
        st.write('Selected State/UT not found in the dataset.')
else:
    st.write('Latitude and Longitude information not available.')


# Summary Statistics for Convicts Data
st.write('### Summary Statistics for Convicts Data')

if selected_states is not None and selected_year is not None:
    total_convicts = convicts_data[(convicts_data['STATE/UT'].isin(selected_states)) & (convicts_data['YEAR'] == selected_year)]['Total Convicts'].sum()
    total_under_trial = convicts_data[(convicts_data['STATE/UT'].isin(selected_states)) & (convicts_data['YEAR'] == selected_year)]['Total Under trial'].sum()
    total_detenues = convicts_data[(convicts_data['STATE/UT'].isin(selected_states)) & (convicts_data['YEAR'] == selected_year)]['Total Detenues'].sum()
    total_others = convicts_data[(convicts_data['STATE/UT'].isin(selected_states)) & (convicts_data['YEAR'] == selected_year)]['Total Others'].sum()

    st.write(f"Total Convicts: {total_convicts}")
    st.write(f"Total Under trial: {total_under_trial}")
    st.write(f"Total Detenues: {total_detenues}")
    st.write(f"Total Others: {total_others}")
else:
    st.write('Please select both State/UT and Year.')



# Stacked Bar Chart for Convicts Data
st.write('### Stacked Bar Chart for Convicts Data')
if selected_states is not None:
    if 'Year' in convicts_data.columns:
        filtered_convicts_data_stacked = convicts_data[convicts_data['STATE/UT'].isin(selected_states)].groupby(['Year', 'STATE/UT']).sum()[['Total Convicts', 'Total Under trial', 'Total Detenues', 'Total Others']].unstack()
        st.bar_chart(filtered_convicts_data_stacked, use_container_width=True)
    else:
        st.write('Year column not found in Convicts Data.')
else:
    st.write('Please select a State/UT.')


# Conclusion
st.write('## Conclusion')

st.write('Thank you for exploring the Public Health Insights App! We hope you gained valuable insights from the data.')

