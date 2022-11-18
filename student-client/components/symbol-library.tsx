import classNames from "classnames";
import Latex from "react-latex";

const SYMBOLS = [
  "\\log_n",
  "a^b",
  "\\Sigma_{i=1}^{n}{i}",
  "\\prod_{i=1}^{n}{i}",
  "\\int_{a}^{b}{i}",
  "\\frac{\\mathrm{d}}{\\mathrm{d} x}",
  "\\frac{\\partial}{\\partial x}",
  "\\frac{a}{b}",
  "\\lim_{n \\to \\infty}{1/x}",
  "O(n)",
  "\\Omega(n)",
  "\\Theta(n)",
  "o(n)",
  "\\omega(n)",
  "\\mathbb{R}",
  "\\mathbb{N}",
  "\\mathbb{Z}",
  "\\forall",
  "\\exists",
  "\\implies",
  "\\impliedby",
  "\\iff",
  "\\therefore",
  "\\approx",
];

interface SymbolLibraryProps {
  symbolClicked?: (symbolLatex: string) => unknown;
  hidden?: boolean;
}

export default function SymbolLibrary(props: SymbolLibraryProps) {
  return (
    <div
      className={classNames(
        "px-4",
        "py-3",
        "bg-white",
        "border-b-2",
        "border-l-2",
        "w-full",
        "max-h-[15vh]",
        "overflow-y-scroll",
        props.hidden && "hidden"
      )}
    >
      {SYMBOLS.map((symbol, idx) => (
        <button
          key={idx}
          className="p-2 min-w-[50px] border-2 mr-4 my-1 rounded-md hover:bg-gray-200"
          onClick={() => props.symbolClicked && props.symbolClicked(symbol)}
        >
          <Latex>{`$${symbol}$`}</Latex>
        </button>
      ))}
    </div>
  );
}
