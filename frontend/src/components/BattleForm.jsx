import { useState, useEffect } from 'react'
import apiService from '../services/api'
import './BattleForm.css'

function BattleForm({ onSubmit, loading, error }) {
  const [personas, setPersonas] = useState([])
  const [formData, setFormData] = useState({
    topic: '',
    persona_A: 'fast_technical',
    persona_B: 'punchline_master',
    rounds: 3,
    description_A: '',
    description_B: '',
  })
  const [loadingPersonas, setLoadingPersonas] = useState(true)
  const [expanded_A, setExpanded_A] = useState(false)
  const [expanded_B, setExpanded_B] = useState(false)

  useEffect(() => {
    loadPersonas()
  }, [])

  const loadPersonas = async () => {
    try {
      const response = await apiService.getPersonas()
      setPersonas(response.personas || [])
      
      if (response.personas && response.personas.length > 0) {
        setFormData(prev => ({
          ...prev,
          persona_A: response.personas[0].id,
          persona_B: response.personas.length > 1 ? response.personas[1].id : response.personas[0].id,
        }))
      }
    } catch (err) {
      console.error('Error loading personas:', err)
    } finally {
      setLoadingPersonas(false)
    }
  }

  const handleChange = (e) => {
    const { name, value } = e.target
    setFormData(prev => ({
      ...prev,
      [name]: name === 'rounds' ? parseInt(value) : value,
    }))
    
    // Si cambia a custom, expandir automáticamente y limpiar descripción adicional si había
    if (name === 'persona_A' && value === 'custom') {
      setExpanded_A(false) // No usar expanded para custom
    } else if (name === 'persona_A' && value !== 'custom') {
      setExpanded_A(false) // Resetear cuando cambia a persona normal
    }
    
    if (name === 'persona_B' && value === 'custom') {
      setExpanded_B(false) // No usar expanded para custom
    } else if (name === 'persona_B' && value !== 'custom') {
      setExpanded_B(false) // Resetear cuando cambia a persona normal
    }
  }

  const handleSubmit = (e) => {
    e.preventDefault()
    if (formData.topic.trim()) {
      // Validar que si es personalizado, tenga descripción adicional
      if (formData.persona_A === 'custom' && !formData.description_A?.trim()) {
        return
      }
      if (formData.persona_B === 'custom' && !formData.description_B?.trim()) {
        return
      }
      
      // Incluir las descripciones de estilo de las personas seleccionadas (solo si no es custom)
      const personaA = formData.persona_A !== 'custom' ? getPersonaInfo(formData.persona_A) : null
      const personaB = formData.persona_B !== 'custom' ? getPersonaInfo(formData.persona_B) : null
      
      const submitData = {
        ...formData,
        style_description_A: personaA?.style_description || null,
        style_description_B: personaB?.style_description || null,
      }
      
      onSubmit(submitData)
    }
  }

  const getPersonaInfo = (personaId) => {
    return personas.find(p => p.id === personaId)
  }

  return (
    <div className="battle-form-container">
      <div className="battle-form-card">
        <h2 className="form-title">Crear Nueva Batalla</h2>
        
        {error && (
          <div className="error-message">
            ⚠️ {error}
          </div>
        )}

        <form onSubmit={handleSubmit} className="battle-form">
          <div className="form-group">
            <label htmlFor="topic" className="form-label">
              Tema de la Batalla
            </label>
            <input
              type="text"
              id="topic"
              name="topic"
              value={formData.topic}
              onChange={handleChange}
              placeholder="Ej: Quién domina más el escenario"
              className="form-input"
              required
              disabled={loading}
            />
          </div>

          <div className="rappers-selection">
            <div className="rapper-select-group">
              <label htmlFor="persona_A" className="form-label">
                Rapero A
              </label>
              {loadingPersonas ? (
                <div className="loading-text">Cargando personalidades...</div>
              ) : (
                <select
                  id="persona_A"
                  name="persona_A"
                  value={formData.persona_A}
                  onChange={handleChange}
                  className="form-select"
                  disabled={loading}
                >
                  {personas.map(persona => (
                    <option key={persona.id} value={persona.id}>
                      {persona.name}
                    </option>
                  ))}
                  <option value="custom">🎨 Personalizado</option>
                </select>
              )}
              {formData.persona_A !== 'custom' && getPersonaInfo(formData.persona_A) && (
                <div className="persona-preview">
                  <p className="persona-description">
                    {getPersonaInfo(formData.persona_A).style_description}
                  </p>
                </div>
              )}
              {formData.persona_A === 'custom' ? (
                <div className="form-group">
                  <label htmlFor="description_A" className="form-label">
                    Descripción del Rapero Personalizado <span style={{color: 'var(--primary)'}}>*</span>
                  </label>
                  <textarea
                    id="description_A"
                    name="description_A"
                    value={formData.description_A}
                    onChange={handleChange}
                    placeholder="Describe el estilo, personalidad y características del rapero..."
                    className="form-textarea"
                    rows="4"
                    required
                    disabled={loading}
                  />
                </div>
              ) : (
                <div className="form-group">
                  <button
                    type="button"
                    className="collapse-toggle"
                    onClick={() => setExpanded_A(!expanded_A)}
                    disabled={loading}
                  >
                    <span className="collapse-toggle-text">
                      {expanded_A ? 'Ocultar' : 'Agregar'} descripción adicional
                    </span>
                    <span className={`collapse-icon ${expanded_A ? 'expanded' : ''}`}>
                      ▼
                    </span>
                  </button>
                  {expanded_A && (
                    <div className="collapsible-content">
                      <label htmlFor="description_A" className="form-label">
                        Descripción adicional del Rapero A (opcional)
                      </label>
                      <textarea
                        id="description_A"
                        name="description_A"
                        value={formData.description_A}
                        onChange={handleChange}
                        placeholder="Ej: Especialista en rimas sobre tecnología y videojuegos"
                        className="form-textarea"
                        rows="3"
                        disabled={loading}
                      />
                    </div>
                  )}
                </div>
              )}
            </div>

            <div className="vs-divider">VS</div>

            <div className="rapper-select-group">
              <label htmlFor="persona_B" className="form-label">
                Rapero B
              </label>
              {loadingPersonas ? (
                <div className="loading-text">Cargando personalidades...</div>
              ) : (
                <select
                  id="persona_B"
                  name="persona_B"
                  value={formData.persona_B}
                  onChange={handleChange}
                  className="form-select"
                  disabled={loading}
                >
                  {personas.map(persona => (
                    <option key={persona.id} value={persona.id}>
                      {persona.name}
                    </option>
                  ))}
                  <option value="custom">🎨 Personalizado</option>
                </select>
              )}
              {formData.persona_B !== 'custom' && getPersonaInfo(formData.persona_B) && (
                <div className="persona-preview">
                  <p className="persona-description">
                    {getPersonaInfo(formData.persona_B).style_description}
                  </p>
                </div>
              )}
              {formData.persona_B === 'custom' ? (
                <div className="form-group">
                  <label htmlFor="description_B" className="form-label">
                    Descripción del Rapero Personalizado <span style={{color: 'var(--primary)'}}>*</span>
                  </label>
                  <textarea
                    id="description_B"
                    name="description_B"
                    value={formData.description_B}
                    onChange={handleChange}
                    placeholder="Describe el estilo, personalidad y características del rapero..."
                    className="form-textarea"
                    rows="4"
                    required
                    disabled={loading}
                  />
                </div>
              ) : (
                <div className="form-group">
                  <button
                    type="button"
                    className="collapse-toggle"
                    onClick={() => setExpanded_B(!expanded_B)}
                    disabled={loading}
                  >
                    <span className="collapse-toggle-text">
                      {expanded_B ? 'Ocultar' : 'Agregar'} descripción adicional
                    </span>
                    <span className={`collapse-icon ${expanded_B ? 'expanded' : ''}`}>
                      ▼
                    </span>
                  </button>
                  {expanded_B && (
                    <div className="collapsible-content">
                      <label htmlFor="description_B" className="form-label">
                        Descripción adicional del Rapero B (opcional)
                      </label>
                      <textarea
                        id="description_B"
                        name="description_B"
                        value={formData.description_B}
                        onChange={handleChange}
                        placeholder="Ej: Conocido por sus referencias a la cultura callejera"
                        className="form-textarea"
                        rows="3"
                        disabled={loading}
                      />
                    </div>
                  )}
                </div>
              )}
            </div>
          </div>

          <div className="form-group">
            <label htmlFor="rounds" className="form-label">
              Número de Rondas: {formData.rounds}
            </label>
            <input
              type="range"
              id="rounds"
              name="rounds"
              min="1"
              max="10"
              value={formData.rounds}
              onChange={handleChange}
              className="form-range"
              disabled={loading}
            />
            <div className="range-labels">
              <span>1</span>
              <span>10</span>
            </div>
          </div>

          <button
            type="submit"
            className="submit-button"
            disabled={loading || !formData.topic.trim()}
          >
            {loading ? (
              <>
                <span className="spinner"></span>
                Iniciando Batalla...
              </>
            ) : (
              <>
                🎤 Iniciar Batalla
              </>
            )}
          </button>
        </form>
      </div>
    </div>
  )
}

export default BattleForm

