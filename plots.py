import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import warnings

warnings.filterwarnings("ignore")

data = pd.read_csv("./Data/data_visualize.csv")
sns.set(style="whitegrid")

def plot_Score():
    fig, ax = plt.subplots(figsize=(10, 6))  # Plot avg_score for different quiz_id
    sns.barplot(x=data.index, y=data["avg_score"], palette="viridis", ax=ax)
    ax.set_title("Average Score by Quiz ID")
    ax.set_xlabel("Quiz ID")
    ax.set_ylabel("Average Score")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    plt.tight_layout()
    return fig

def plot_Accuracy():
    fig, ax = plt.subplots(figsize=(10, 6))  # Plot avg_accuracy for different quiz_id
    sns.barplot(x=data.index, y=data["avg_accuracy"], palette="muted", ax=ax)
    ax.set_title("Average Accuracy by Quiz ID")
    ax.set_xlabel("Quiz ID")
    ax.set_ylabel("Average Accuracy")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    plt.tight_layout()
    return fig

def plot_Time():
    fig, ax = plt.subplots(figsize=(10, 6))  # Plot avg_time for different quiz_id
    sns.barplot(x=data.index, y=data["avg_time"], palette="coolwarm", ax=ax)
    ax.set_title("Average Time Taken by Quiz ID")
    ax.set_xlabel("Quiz ID")
    ax.set_ylabel("Average Time (minutes)")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    plt.tight_layout()
    return fig

def plot_Mistake_Count():
    fig, ax = plt.subplots(figsize=(10, 6))  # Plot avg_initial_mistake_count for different quiz_id
    sns.barplot(x=data.index, y=data["avg_initial_mistake_count"], palette="pastel", ax=ax)
    ax.set_title("Average Initial Mistake Count by Quiz ID")
    ax.set_xlabel("Quiz ID")
    ax.set_ylabel("Average Initial Mistake Count")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    plt.tight_layout()
    return fig