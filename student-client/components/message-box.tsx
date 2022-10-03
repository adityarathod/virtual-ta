import classNames from "classnames";
import { useEffect, useRef, useState } from "react";
import Latex from "react-latex";
import SymbolLibrary from "./symbol-library";

interface MessageBoxProps {
  onSend: (newMessage: string, containsMath: boolean) => unknown;
}

export default function MessageBox({ onSend }: MessageBoxProps) {
  const [msg, setMsg] = useState<string>("");
  const inputBoxRef = useRef<HTMLInputElement>(null);
  const [containsMath, setContainsMath] = useState<boolean>(false);
  const [symbolLibraryOpen, setSymbolLibraryOpen] = useState<boolean>(false);

  useEffect(() => {
    setContainsMath(msg.includes("$"));
  }, [msg]);

  return (
    <section>
      {containsMath && (
        <div className="px-4 py-3 bg-white border-b-2">
          <h3 className="text-lg font-semibold mb-2">Rendered Math Preview</h3>
          <p>
            <Latex>{msg}</Latex>
          </p>
        </div>
      )}
      <SymbolLibrary
        symbolClicked={(symbolLatex) => {
          setMsg(msg + ` $${symbolLatex}$`);
          inputBoxRef.current.focus();
        }}
        hidden={!symbolLibraryOpen}
      />
      <form
        className="flex flex-row bg-white items-center"
        onSubmit={(e) => {
          if (msg.trim().length > 0) {
            onSend(msg.trim(), containsMath || msg.includes("$"));
            setMsg("");
          }
          e.preventDefault();
        }}
      >
        <input
          type="text"
          className="bg-white px-4 py-3 w-full text-md outline-none"
          placeholder="what's the runtime of insertion sort?"
          value={msg}
          onChange={(e) => {
            const newMsg = e.target.value;
            setMsg(newMsg);
          }}
          ref={inputBoxRef}
        />
        <div className="px-4 flex flex-row items-center">
          <div
            className={classNames(
              "font-serif",
              "text-2xl",
              symbolLibraryOpen ? "text-teal-500" : "text-gray-400",
              symbolLibraryOpen ? "hover:text-gray-400" : "hover:text-teal-500",
              "mr-4",
              "cursor-pointer",
              "select-none"
            )}
            onClick={(e) => {
              setSymbolLibraryOpen(!symbolLibraryOpen);
              e.preventDefault();
            }}
          >
            Σ
          </div>
          <input
            type="submit"
            value="Send"
            className="font-bold text-md"
            style={{ color: "#1982FC" }}
          />
        </div>
      </form>
    </section>
  );
}
