import React from 'react';
import { render, screen } from '@testing-library/react';
import About from '../components/About';

test('renders mission statement', () => {
  render(<About />);
  const missionElement = screen.getByText(/Providing compassionate care/i);
  expect(missionElement).toBeInTheDocument();
});

test('renders team mantra', () => {
  render(<About />);
  const mantraElement = screen.getByText(/Together, we’re the heartbeat of healthcare/i);
  expect(mantraElement).toBeInTheDocument();
});

test('renders vision statement', () => {
  render(<About />);
  const visionElement = screen.getByText(/To lead the future of healthcare/i);
  expect(visionElement).toBeInTheDocument();
});
