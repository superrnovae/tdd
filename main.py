import argparse
from src.data_loader import DataLoader
from src.analyzer import DataAnalyzer
from src.visualizer import DataVisualizer

def main():
    parser = argparse.ArgumentParser(description="Data Analyzer Application")
    parser.add_argument('file', type=str, help='Path to the input data file')
    parser.add_argument('--analysis', type=str, choices=['summary', 'detailed'], required=True, help='Type of analysis to perform')
    parser.add_argument('--plot', type=str, choices=['bar', 'line', 'scatter'], required=True, help='Type of plot to generate')
    parser.add_argument('--output', type=str, required=True, help='Path to save the output results')

    args = parser.parse_args()

    print(args.file)

    # Use DataLoader class to load the data
    data_loader = DataLoader(args.file)
    data_loader.load_data()
    data = data_loader.data

    if data is None:
        print("Failed to load data.")
        return

    # Use Analyzer class to perform analysis
    analyzer = DataAnalyzer(data)
    analysis_results = analyzer.summary_statistics('category', 'amount')

    # Use Visualizer class to generate the plot
    visualizer = DataVisualizer(analysis_results)
    visualizer.bar_chart('category', 'amount', title='Category Amount Distribution', save_path= 'data/results/bar_chart.png')
    
    print(f"Analysis and plot generation completed. Results saved to: {args.output}")

if __name__ == "__main__":
    main()