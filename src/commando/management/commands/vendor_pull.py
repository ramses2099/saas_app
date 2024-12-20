from typing import Any

from django.conf import settings
from django.core.management.base import BaseCommand

import helpers

STATIC_VENDORS_DIR = getattr(settings, 'STATIC_VENDORS_DIR')

VENDOR_STATICFIELS ={
  "flowbite.min.cs":"https://cdn.jsdelivr.net/npm/flowbite@2.5.2/dist/flowbite.min.css",
  "flowbite.min.js":"https://cdn.jsdelivr.net/npm/flowbite@2.5.2/dist/flowbite.min.js"
}

class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> str | None:
        self.stdout.write("Downloading vendor statis files")
        completed_urls = []
        for name, url in VENDOR_STATICFIELS.items():
            out_path = STATIC_VENDORS_DIR / name
            dl_success = helpers.download_to_local(url, out_path)
            if dl_success:
                completed_urls.append(url)
            else:
                self.stdout.write(
                    self.style.ERROR(f'Faild to download {url}'))
                
        if set(completed_urls)== set(VENDOR_STATICFIELS.values()):
            self.stdout.write(self.style.SUCCESS('Successfully updated vendor statis files'))
        else:
            self.stdout.write(self.style.WARNING('Some file were not updated'))
