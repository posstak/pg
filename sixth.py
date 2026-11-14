import sys
import requests
import re

def download_url_and_get_all_hrefs(url):
    """
    Funkce stahne url predanou v parametru url pomoci volani response = requests.get(),
    zkontroluje navratovy kod response.status_code, ktery musi byt 200,
    pokud ano, najdete ve stazenem obsahu stranky response.content vsechny vyskyty
    <a href="url">odkaz</a> a z nich nactete url, ktere vratite jako seznam pomoci return
    """

    hrefs:list[str] = []
    response = requests.get(url)
    if (response.status_code == 404):
        print("Chyba 404 - stránka se zadnou URL neexistuje.")
        return []
    elif (response.status_code != 200):
        print(f"Chyba {response.status_code}")
        return []
    data = response.text
    pattern = r'<a\s+(?:[^>]*?\s+)?href=["\'](.*?)["\']' # Zdroj Gemini 💀
    hrefs = re.findall(pattern, data, re.IGNORECASE)
    print(f"Delka seznamu odkazu je {len(hrefs)}.")

    return hrefs

if __name__ == "__main__":
    try:
        download_url_and_get_all_hrefs(sys.argv[1])
    # osetrete potencialni chyby pomoci vetve except
    except IndexError:
        print("Nebyl zadan parametr (URL pozadovane stranky).")
    except Exception as e:
        print(f"Program skoncil jinou chybou: {e}")
