import { useState } from "react";

interface MessageBoxProps {
  onSend: (newMessage: string) => unknown;
}

export default function MessageBox({ onSend }: MessageBoxProps) {
  const [msg, setMsg] = useState<string>("");
  return (
    <section>
      <form
        className="flex flex-row bg-white items-center"
        onSubmit={(e) => {
          if (msg.trim().length > 0) {
            onSend(msg.trim());
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
          onChange={(e) => setMsg(e.target.value)}
        />
        <div className="px-4">
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
