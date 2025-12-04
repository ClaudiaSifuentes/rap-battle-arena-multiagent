import { useState } from 'react'
import './BattleResults.css'

function BattleResults({ result, onNewBattle }) {
  const [expandedRound, setExpandedRound] = useState(null)

  const toggleRound = (roundNumber) => {
    setExpandedRound(expandedRound === roundNumber ? null : roundNumber)
  }

  const getWinnerClass = (winner) => {
    if (winner === 'A') return 'winner-a'
    if (winner === 'B') return 'winner-b'
    return 'winner-draw'
  }

  const getOverallWinnerClass = () => {
    return getWinnerClass(result.overall_winner)
  }

  return (
    <div className="battle-results-container">
      <div className="battle-results-header">
        <h2 className="battle-topic">🎯 {result.topic}</h2>
        <div className={`overall-winner ${getOverallWinnerClass()}`}>
          {result.overall_winner === 'draw' ? (
            <>
              <span className="winner-icon">🤝</span>
              <span>Empate</span>
            </>
          ) : (
            <>
              <span className="winner-icon">🏆</span>
              <span>Ganador: Rapero {result.overall_winner}</span>
            </>
          )}
        </div>
        <button onClick={onNewBattle} className="new-battle-button">
          🎤 Nueva Batalla
        </button>
      </div>

      <div className="rounds-container">
        {result.rounds.map((round, index) => (
          <div key={round.round_number} className="round-card">
            <div 
              className="round-header"
              onClick={() => toggleRound(round.round_number)}
            >
              <div className="round-info">
                <span className="round-number">Ronda {round.round_number}</span>
                <div className="round-scores">
                  <span className={`score score-a ${round.winner === 'A' ? 'winner' : ''}`}>
                    A: {round.score_A.toFixed(3)}
                  </span>
                  <span className="score-divider">vs</span>
                  <span className={`score score-b ${round.winner === 'B' ? 'winner' : ''}`}>
                    B: {round.score_B.toFixed(3)}
                  </span>
                </div>
              </div>
              <div className={`round-winner ${getWinnerClass(round.winner)}`}>
                {round.winner === 'draw' ? '🤝 Empate' : `🏆 Ganador: ${round.winner}`}
              </div>
              <span className="expand-icon">
                {expandedRound === round.round_number ? '▼' : '▶'}
              </span>
            </div>

            {expandedRound === round.round_number && (
              <div className="round-content">
                <div className="verses-container">
                  <div className={`verse-card verse-a ${round.winner === 'A' ? 'winner-verse' : ''}`}>
                    <div className="verse-header">
                      <span className="verse-label">Rapero A</span>
                      <span className="verse-score">Score: {round.score_A.toFixed(3)}</span>
                    </div>
                    <div className="verse-text">
                      {round.verse_A.text.split('\n').map((line, i) => (
                        <p key={i} className="verse-line">{line}</p>
                      ))}
                    </div>
                  </div>

                  <div className={`verse-card verse-b ${round.winner === 'B' ? 'winner-verse' : ''}`}>
                    <div className="verse-header">
                      <span className="verse-label">Rapero B</span>
                      <span className="verse-score">Score: {round.score_B.toFixed(3)}</span>
                    </div>
                    <div className="verse-text">
                      {round.verse_B.text.split('\n').map((line, i) => (
                        <p key={i} className="verse-line">{line}</p>
                      ))}
                    </div>
                  </div>
                </div>
              </div>
            )}
          </div>
        ))}
      </div>
    </div>
  )
}

export default BattleResults

