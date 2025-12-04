import { useState } from 'react'
import BattleForm from './components/BattleForm'
import BattleResults from './components/BattleResults'
import Header from './components/Header'
import apiService from './services/api'
import './App.css'

function App() {
  const [battleResult, setBattleResult] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  const handleBattleSubmit = async (battleData) => {
    setLoading(true)
    setError(null)
    setBattleResult(null)

    try {
      const result = await apiService.startBattle(battleData)
      setBattleResult(result)
    } catch (err) {
      setError(err.message || 'Error al iniciar la batalla')
      console.error('Battle error:', err)
    } finally {
      setLoading(false)
    }
  }

  const handleNewBattle = () => {
    setBattleResult(null)
    setError(null)
  }

  return (
    <div className="app">
      <Header />
      <main className="main-content">
        {!battleResult ? (
          <BattleForm 
            onSubmit={handleBattleSubmit} 
            loading={loading}
            error={error}
          />
        ) : (
          <BattleResults 
            result={battleResult} 
            onNewBattle={handleNewBattle}
          />
        )}
      </main>
    </div>
  )
}

export default App

