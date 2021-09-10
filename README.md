# Khmer Auto Zero-width Space

Credits to [danhhong/khmer_segment](https://github.com/danhhong/khmer_segment)

[![Create and publish a Docker image](https://github.com/pigeon-media/khmer-auto-zwsp/actions/workflows/build-publish.yml/badge.svg)](https://github.com/pigeon-media/khmer-auto-zwsp/actions/workflows/build-publish.yml)

### Usage

The server will be running on `http://localhost:5000`

#### Request

```json
{ "data": "កូនខ្មែរគឺជាមនុស្សខ្មែរ" }
```


#### Response

```json
{
  "data": [
    "កូនខ្មែរ",
    "គឺជា",
    "មនុស្ស",
    "ខ្មែរ"
  ]
}
```
