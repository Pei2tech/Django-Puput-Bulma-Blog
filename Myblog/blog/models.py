from django.db import models
from django.utils.translation import ugettext_lazy as _
from puput.abstracts import EntryAbstract,BlogAbstract

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import RichTextField
from colorful.fields import RGBColorField
from wagtailmarkdown.edit_handlers import MarkdownPanel
from wagtailmarkdown.fields import MarkdownField

# Create your models here.


class MakeBlog(BlogAbstract):
    label_color = RGBColorField(_('Blog Title Color'),blank=True)
    head_color = RGBColorField(_('Blog Head Color'), default="#FEFEFF",blank=True)
    body_color = RGBColorField(_('Blog Body Color'), default="#FFFFFF",blank=True)
    background_url = models.URLField(blank=True)
    content_panels = BlogAbstract.content_panels + [
        FieldPanel('label_color'),
        FieldPanel('head_color'),
        FieldPanel('body_color'),
        FieldPanel('background_url')
    ]
    class Meta:
        abstract = True

class MarkdownEntryAbstract(EntryAbstract):
    video_url = models.URLField(blank=True)
    body = MarkdownField(verbose_name=_('body'))
    excerpt = RichTextField(verbose_name=_('excerpt'),blank=True)

    content_panels = [
        MultiFieldPanel(
            [
                FieldPanel('title', classname="title"),
                ImageChooserPanel('header_image'),
                FieldPanel('video_url'),
                MarkdownPanel('body', classname="full"),
                FieldPanel('excerpt', classname="full"),
            ],
            heading=_("Content")
        ),
        MultiFieldPanel(
            [
                FieldPanel('tags'),
                InlinePanel('entry_categories', label=_("Categories")),
                InlinePanel(
                    'related_entrypage_from',
                    label=_("Related Entries"),
                    panels=[PageChooserPanel('entrypage_to')]
                ),
            ],
            heading=_("Metadata")),
    ]
    class Meta:
        abstract = True
