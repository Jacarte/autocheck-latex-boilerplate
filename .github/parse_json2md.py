
import json
import sys

def process(f, tex):
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

        print("- [*%s*](https://github.com/Jacarte/CROW-paper/blob/fd1f5ce9196402fd7cad498ca3ce9e9aee3698ee/main.tex#L%s) %s\n  %s"%(error,n, message, rule))
        pass

if __name__ == "__main__":
    process(sys.argv[1], sys.argv[2])