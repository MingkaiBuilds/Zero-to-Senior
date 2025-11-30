type StudyListProps = {
    sessions: string[];
};

export function StudyList({ sessions }: StudyListProps) {
    return (
        <ul>
            {sessions.map((s, i) => <li key={i}>{s}</li>)}
        </ul>
    );
}