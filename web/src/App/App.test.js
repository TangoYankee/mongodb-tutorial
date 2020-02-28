import React from 'react'
import { render } from '@testing-library/react'
import App from './App'

it('renders the title of the website', () => {
  const { getByText } = render(<App />)
  const headerOne = getByText(/Phoenix Spark/)
  expect(headerOne).toBeInTheDocument()
})
