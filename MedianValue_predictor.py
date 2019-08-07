{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "MedianValue_predictor.ipynb",
      "version": "0.3.2",
      "provenance": [],
      "collapsed_sections": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "metadata": {
        "id": "oUGQDfGI--1l",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "from statistics import median"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "I3G2BbskG5Kb",
        "colab_type": "code",
        "outputId": "ce45bdbb-f228-441e-c5b8-0766f65a19ff",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "median([5, 2, 3, 8, 9, -2])\n"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "4.0"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 3
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "qOdfvlMTHJce",
        "colab_type": "code",
        "outputId": "820fcf03-3dc4-4d3c-bdfe-9b58c3d9718b",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "# length of list\n",
        "\n",
        "length = int(input(\"Enter the length of list \"))\n",
        "while length % 2 != 0 or length < 6:\n",
        "   length = int(input(\"Please enter even size greater than 6 for the list\"))\n"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Enter the length of list 6\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "CkD0vRgOKN3U",
        "colab_type": "code",
        "outputId": "a8bc2a80-cc20-4fb3-be01-5a21c02788ba",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 255
        }
      },
      "source": [
        "a = []\n",
        "for i in range(length):\n",
        "    print(\"Input list element \" ,i+1) \n",
        "    a.append(int(input(\" \")))\n",
        "    if i != 0:\n",
        "      while a[i-1]>a[i]:\n",
        "        print(\"Input list element \" ,i+1 , \"needs to greater than input list element\", i ,\"which is \",a[i-1],\"\\n Enter new input\" ) \n",
        "        a[i] = (int(input(\" \")))\n",
        "        break\n",
        "\n",
        "print(a)\n",
        "median(a)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Input list element  1\n",
            " 1\n",
            "Input list element  2\n",
            " 1\n",
            "Input list element  3\n",
            " 1\n",
            "Input list element  4\n",
            " 6\n",
            "Input list element  5\n",
            " 6\n",
            "Input list element  6\n",
            " 6\n",
            "[1, 1, 1, 6, 6, 6]\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "3.5"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 6
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "TfqWViakPMs5",
        "colab_type": "code",
        "outputId": "01bb2232-15ca-4882-d7f4-69829b322090",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 51
        }
      },
      "source": [
        "a.sort()\n",
        "print(a)\n",
        "median(a)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[2, 3, 4, 5, 7, 8]\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "4.5"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 46
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Ged7RkZfW9Z1",
        "colab_type": "text"
      },
      "source": [
        "value_predictor([1,2,3,4,5,6]) should return 3.5\n",
        "value_predictor([1,1,1,6,6,6]) should return either 3.5 closer to 3.45 depending on method\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "G_SFFHvqQkco",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        ""
      ],
      "execution_count": 0,
      "outputs": []
    }
  ]
}