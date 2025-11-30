import { useState } from "react";

type StudyInputProps = {
    onAdd: (name: string) => void;
};

export function StudyInput({ onAdd }: StudyInputProps) {
    const [text, setText] = useState("");

    return (
        <div>
            <input value={text} onChange={(e) => setText(e.target.value)} placeholder="Study session name" />
            <button onClick={() => {
                if (text.trim().length === 0) return;
                onAdd(text);
                setText("");
            }}>
                Add
            </button>
        </div>
    );
}