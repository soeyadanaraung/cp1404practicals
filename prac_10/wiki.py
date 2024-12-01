import warnings
import wikipedia

# Suppress BeautifulSoup warnings
warnings.filterwarnings("ignore", category=UserWarning, module='wikipedia')

def main():
    """Prompt the user for a Wikipedia page title or search phrase, and display details."""
    while True:
        search_query = input("Enter page title: ").strip()
        if not search_query:
            print("Thank you.")
            break

        try:
            # Try to fetch a Wikipedia page with the given title
            page = wikipedia.page(search_query, auto_suggest=False)
            print(f"\n{page.title}")
            print(f"{page.summary[:500]}...\n{page.url}\n")
        except wikipedia.exceptions.PageError:
            # Handle PageError when no match is found
            print(f'Page id "{search_query}" does not match any pages. Try another id!\n')
        except wikipedia.exceptions.DisambiguationError as e:
            # Handle DisambiguationError when a more specific page title is needed
            print("We need a more specific title. Try one of the following, or a new search:")
            print("(BeautifulSoup warning)")
            options = e.options[:5]  # Limit to first 5 disambiguation options
            print(f"{options}...\n")
        except Exception as e:
            # Catch-all for unexpected errors
            print(f"An unexpected error occurred: {e}\n")

if __name__ == "__main__":
    main()









