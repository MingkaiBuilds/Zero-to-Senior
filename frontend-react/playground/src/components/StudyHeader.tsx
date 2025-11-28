import React from "react";

type StudyHeaderProps = {
    title: string;
};

export function StudyHeader({ title }: StudyHeaderProps) {
    return (
        <p>{title}</p>
    );
}