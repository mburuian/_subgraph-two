from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# URL of your subgraph API
SUBGRAPH_URL = "https://api.studio.thegraph.com/query/89385/alx_sub/version/latest"

def query_subgraph(query):
    """Send a GraphQL query to the subgraph and return the response."""
    try:
        response = requests.post(SUBGRAPH_URL, json={'query': query})
        response.raise_for_status()  # Raise an exception for 4xx/5xx errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error querying the subgraph: {e}")
        return {}

@app.route('/')
def home():
    query = """
    {
      transfers(
        where: { 
          blockNumber_gte: "20826020", 
          blockNumber_lte: "20826708"
        }, 
        orderBy: blockTimestamp, 
        orderDirection: desc
      ) {
        id
        from
        to
        transactionHash
        blockTimestamp
      }
    }
    """
    result = query_subgraph(query)
    
    # Safeguard: Check if 'data' and 'transfers' keys exist in the result
    transactions = result.get('data', {}).get('transfers', [])
    
    return render_template('index.html', transactions=transactions)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
