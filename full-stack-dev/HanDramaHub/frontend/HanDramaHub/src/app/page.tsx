export default async function Home() {
  const res = await fetch("http://127.0.0.1:8000/health/", { cache: "no-store" });

  if (!res.ok) {
    return (
      <main>
        <h1>Backend health check failed.</h1>
        <p>Status: {res.status}</p>
      </main>
    );
  }

  const data = await res.json();

  return (
    <main>
      <h1>HanDramaHub</h1>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </main>
  );
}