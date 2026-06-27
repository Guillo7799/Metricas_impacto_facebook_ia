from ucimlrepo import fetch_ucirepo

facebook_metrics = fetch_ucirepo(id=368)

X = facebook_metrics.data.features
y = facebook_metrics.data.targets