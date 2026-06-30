"use client";

import { useState } from "react";

type Card = {
  id: number;
  player: string;
  year: number;
  brand: string;
  card_number: string;
  grade: string;
  estimated_value: number;
};

export default function Home() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState<Card[]>([]);
  const [loading, setLoading] = useState(false);

  async function handleSearch() {
    if (!query.trim()) return;

    setLoading(true);

    try {
      const response = await fetch(
        `http://127.0.0.1:8000/cards/search?query=${encodeURIComponent(query)}`
      );

      const data = await response.json();
      setResults(data.results);
    } catch (error) {
      console.error(error);
      alert("Unable to connect to the backend.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="min-h-screen bg-slate-950 text-white">
      <div className="max-w-5xl mx-auto px-6 py-16">

        <h1 className="text-5xl font-bold text-center">
          🏀 CardValue AI
        </h1>

        <p className="text-center text-gray-400 mt-4 mb-10">
          Search real basketball card values from sold listings.
        </p>

        <div className="flex gap-3 mb-10">
          <input
            className="flex-1 rounded-lg border border-gray-700 bg-slate-900 px-4 py-3"
            placeholder="Example: 2023 Prizm Wembanyama PSA 10"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
          />

          <button
            onClick={handleSearch}
            className="bg-blue-600 hover:bg-blue-700 px-6 rounded-lg font-semibold"
          >
            {loading ? "Searching..." : "Search"}
          </button>
        </div>

        <div className="space-y-5">
          {results.map((card) => (
            <div
              key={card.id}
              className="rounded-xl bg-slate-900 p-6 border border-slate-700"
            >
              <h2 className="text-2xl font-bold">
                {card.year} {card.brand}
              </h2>

              <p className="mt-2">
                <strong>Player:</strong> {card.player}
              </p>

              <p>
                <strong>Card #:</strong> {card.card_number}
              </p>

              <p>
                <strong>Grade:</strong> {card.grade}
              </p>

              <p className="text-green-400 text-2xl font-bold mt-4">
                Estimated Value: $
                {card.estimated_value.toLocaleString()}
              </p>
            </div>
          ))}
        </div>

      </div>
    </main>
  );
}