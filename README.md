# RASD - Reliability Analysis for Structural Design [EN-US]

## Overview

**RASD** (Reliability Analysis for Structural Design) is a Python-based computational library developed to perform reliability analysis for structural design problems. It integrates various open-source tools and libraries, including **SciPy**, **Matplotlib**, and **NumPy**.

This library was developed as part of a **master's thesis** and aims to evaluate the limit state functions for reliability problems, determining the **reliability index** and the **probability of failure** for structural systems.

## Key Features

- **Monte Carlo Simulation** and **Latin Hypercube Sampling**: These techniques are used to generate random samples with probabilistic distributions, including normal, log-normal, Gumbel, and uniform distributions.
  
- **Limit State Function Evaluation**: RASD allows you to evaluate the limit state functions based on the generated samples.

- **Graphical Results**: The library generates visualizations using **Matplotlib** to display the simulation results, including:
  - **Histograms**: Showing the frequency distribution of the generated numerical values.
  - **Scatter Plots**: Displaying the relationship between two numeric variables.
  - **Performance Function Dispersion Graphs**: Representing the dispersion of the samples in the performance function.

## Methodology

- **Reliability Indices and Failure Probability**: The primary goal is to determine the reliability index and failure probability of structural systems using probabilistic methods.
- **Sample Generation**: Users can choose between Monte Carlo and Latin Hypercube methods to generate samples based on various statistical distributions.



# RASD - Análise de Confiabilidade para Projeto Estrutural [PT-BR]

## Visão Geral

O **RASD** (Reliability Analysis for Structural Design) é uma biblioteca computacional desenvolvida em Python, projetada para realizar análises de confiabilidade em problemas de projeto estrutural. Ela integra diversas ferramentas e bibliotecas open-source, como **SciPy**, **Matplotlib** e **NumPy**.

Esta biblioteca foi desenvolvida como parte da minha **dissertação de mestrado** e tem como objetivo principal avaliar as funções de estado limite para problemas de confiabilidade, determinando os **índices de confiabilidade** e a **probabilidade de falha** de sistemas estruturais.

## Funcionalidades Principais

- **Simulação de Monte Carlo** e **Amostragem Hipercubo Latino**: Técnicas utilizadas para gerar amostras aleatórias com distribuições probabilísticas, incluindo distribuições normal, log-normal, Gumbel e uniforme.
  
- **Avaliação de Função de Estado Limite**: O RASD permite avaliar as funções de estado limite com base nas amostras geradas.

- **Resultados Gráficos**: A biblioteca gera visualizações utilizando **Matplotlib** para exibir os resultados das simulações, incluindo:
  - **Histogramas**: Exibindo a distribuição de frequência dos valores numéricos gerados.
  - **Gráficos de Dispersão**: Mostrando a relação entre duas variáveis numéricas.
  - **Gráficos de Dispersão da Função de Desempenho**: Representando a dispersão das amostras na função de desempenho.

## Metodologia

- **Índices de Confiabilidade e Probabilidade de Falha**: O principal objetivo é determinar o índice de confiabilidade e a probabilidade de falha dos sistemas estruturais usando métodos probabilísticos.
- **Geração de Amostras**: O usuário pode escolher entre os métodos de Monte Carlo e Hipercubo Latino para gerar as amostras, com diversas distribuições estatísticas.

