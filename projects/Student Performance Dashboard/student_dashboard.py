
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random
import string

# Generate random student data
def generate_students_csv(filename, num_students=200):
    names = []
    for _ in range(num_students):
        name = ''.join(random.choices(string.ascii_uppercase, k=1)) + ''.join(random.choices(string.ascii_lowercase, k=4))
        names.append(name)
    data = {
        'Name': names,
        'Math': [random.randint(40, 100) for _ in range(num_students)],
        'English': [random.randint(40, 100) for _ in range(num_students)],
        'Science': [random.randint(40, 100) for _ in range(num_students)]
    }
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Generated {filename} with {num_students} students.")

# Load data from CSV
def load_data(filename):
    return pd.read_csv(filename)

# Calculate averages and insights
def analyze_data(df):
    df['Average'] = df.iloc[:, 1:].mean(axis=1)
    best_student = df.loc[df['Average'].idxmax()]
    worst_student = df.loc[df['Average'].idxmin()]
    subject_averages = df.iloc[:, 1:-1].mean()
    return best_student, worst_student, subject_averages

# Plot graphs
def plot_graphs(df, subject_averages):
    # Use a single axis for all charts with navigation
    from matplotlib.widgets import Button

    fig, ax = plt.subplots(figsize=(12, 8))
    plt.subplots_adjust(bottom=0.22)

    chart_titles = [
        'Average Marks per Student',
        'Subject Performance Comparison',
        'Average Marks per Subject',
        'Distribution of All Marks'
    ]
    chart_filenames = [
        'average_marks_per_student.png',
        'subject_performance_comparison.png',
        'average_marks_per_subject.png',
        'marks_distribution.png'
    ]

    def draw_plot(idx):
        ax.clear()
        if idx == 0:
            # Barplot: Average marks per student (top 50), show student names, fix palette warning
            sns.barplot(x='Name', y='Average', data=df, ax=ax, hue='Name', palette='viridis', legend=False)
            ax.set_title(chart_titles[0], fontsize=18)
         
            ax.set_ylabel('Average Marks', fontsize=14)
            ax.set_xticks(range(len(df['Name'])))
            ax.set_xticklabels(df['Name'], rotation=90, fontsize=8)
            for i, v in enumerate(df['Average']):
                ax.text(i, v + 0.5, f"{v:.1f}", ha='center', va='bottom', fontsize=8, rotation=90)
        elif idx == 1:
            # Line plot: Subject performance comparison, show marks as points and lines
            colors = ['#e41a1c', '#377eb8', '#4daf4a']
            for i, subject in enumerate(df.columns[1:-1]):
                ax.plot(df['Name'], df[subject], label=subject, color=colors[i % len(colors)], marker='o', linewidth=2)
                for j, mark in enumerate(df[subject]):
                    ax.text(j, mark + 0.5, f"{mark}", ha='center', va='bottom', fontsize=7, color=colors[i % len(colors)])
            ax.set_title(chart_titles[1], fontsize=18)
         
            ax.set_ylabel('Marks', fontsize=14)
            ax.set_xticks(range(len(df['Name'])))
            ax.set_xticklabels(df['Name'], rotation=90, fontsize=8)
            ax.legend(fontsize=12)
        elif idx == 2:
            # Barplot: Average marks per subject (clear, with values), add legend for colors, fix palette warning
            subject_colors = ['#e41a1c', '#377eb8', '#4daf4a']
            bars = sns.barplot(x=subject_averages.index, y=subject_averages.values, ax=ax, hue=subject_averages.index, palette=subject_colors, legend=False)
            ax.set_title(chart_titles[2], fontsize=18)
            ax.set_xlabel('Subject', fontsize=14)
            ax.set_ylabel('Average Marks', fontsize=14)
            for bar, value, subject, color in zip(bars.patches, subject_averages.values, subject_averages.index, subject_colors):
                ax.text(bar.get_x() + bar.get_width() / 2, value + 0.5, f"{value:.1f}", ha='center', va='bottom', fontsize=12, color=color)
            ax.set_ylim(0, 110)
            # Add manual legend for subject colors
            from matplotlib.patches import Patch
            legend_elements = [Patch(facecolor=color, label=subject) for color, subject in zip(subject_colors, subject_averages.index)]
            ax.legend(handles=legend_elements, title="Subject", fontsize=12)
        elif idx == 3:
            # Histogram: Distribution of all marks
            all_marks = pd.concat([df['Math'], df['English'], df['Science']])
            ax.hist(all_marks, bins=12, color='#377eb8', edgecolor='black', alpha=0.7)
            ax.set_title(chart_titles[3], fontsize=18)
            ax.set_xlabel('Marks', fontsize=14)
            ax.set_ylabel('Number of Occurrences', fontsize=14)
        fig.canvas.draw()

    current_plot = [0]
    draw_plot(current_plot[0])

    # Place navigation buttons perfectly centered below the plot area
    button_width = 0.035
    button_height = 0.035
    center_x = 0.5
    y_pos = 0.01  # Lower for more space
    axprev = plt.axes([center_x - 0.045, y_pos, button_width, button_height])
    axnext = plt.axes([center_x + 0.01, y_pos, button_width, button_height])
    bnext = Button(axnext, '>', color='lightgray', hovercolor='gray')
    bprev = Button(axprev, '<', color='lightgray', hovercolor='gray')

    def next_plot(event):
        current_plot[0] = (current_plot[0] + 1) % 4
        draw_plot(current_plot[0])

    def prev_plot(event):
        current_plot[0] = (current_plot[0] - 1) % 4
        draw_plot(current_plot[0])

    bnext.on_clicked(next_plot)
    bprev.on_clicked(prev_plot)
    plt.show()

def main():
    # Use only the first 50 students from the CSV for clarity
    filename = "students.csv"
    df = load_data(filename).head(50)
    best, worst, subject_averages = analyze_data(df)
    print(f"Best Student: {best['Name']} (Average: {best['Average']:.2f})")
    print(f"Worst Student: {worst['Name']} (Average: {worst['Average']:.2f})")
    print("\nSubject Averages:")
    print(subject_averages)
    plot_graphs(df, subject_averages)

if __name__ == "__main__":
    main()
