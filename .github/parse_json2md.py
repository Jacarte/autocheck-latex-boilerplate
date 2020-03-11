
import json
import sys

def process(f, tex, revision):
    issues = json.loads(open(f, 'r').read())
    file = open(tex, 'r').read()

    # language issues

    print("## %s Warnings"%(len(issues["matches"])))

    for m in issues["matches"]:
        sentence = m["sentence"]
        rule = m["rule"]["description"]
        message = m["message"]
        position = m["offset"]
        length = m["length"]
        
        error = file[position:position + length]

        # estimating line
        prev = file[:position]
        n = len(prev.split("\n"))

        repo = 'https://github.com/Jacarte/autocheck-latex-boilerplate'

        print(f"- [ ] [*{error}*]({repo}/blob/{revision}/{tex}#L{n}) {message}\n  {rule}")
        pass

if __name__ == "__main__":
    process(*sys.argv[1:])